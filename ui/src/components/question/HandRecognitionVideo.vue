<template>
    <div>
        <video ref="video" autoplay></video>
    </div>
</template>

<script>
import * as fp from 'fingerpose';
import * as handpose from '@tensorflow-models/handpose';
import thumbsDownGesture from './ThumbsDownGesture';

require('@tensorflow/tfjs-backend-webgl');

export default {
    name: 'HandRecognitionVideo',
    props: {
        handleGesture: {
            type: Function,
            required: true,
        },
    },
    data() {
        return {
            currentVideo: null,
            currentEstimateHandsId: null
        };
    },
    mounted() {
        this.startVideoStream();
        this.isRecognitionActivated = true;
        this.startRecognition()
    },
    beforeUnmount() {
        console.log("before")
        clearTimeout(this.currentEstimateHandsId)
        this.stopVideoStream();
    },
    methods: {
        async startVideoStream() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                this.$refs.video.srcObject = stream;
            } catch (error) {
                console.error('Error accessing camera:', error);
            }
        },
        async startRecognition() {
            const model = await handpose.load();
            const videoElement = this.$refs.video;
            const GE = new fp.GestureEstimator([
                fp.Gestures.ThumbsUpGesture,
                thumbsDownGesture,
            ]);
            
            const estimateHands = async () => {
                const predictions = await model.estimateHands(videoElement, true);
                if (predictions.length > 0) {
                    const estimatedGestures = GE.estimate(predictions[0].landmarks, 8.5);
                    
                    if (estimatedGestures.gestures.length > 0) {
                        let highestScoreGesture = estimatedGestures.gestures.reduce((p, c) => {
                            return (p.score > c.score) ? p : c
                        })
                        
                        this.handleGesture(highestScoreGesture.name);
                    }
                } else {
                    this.handleGesture('');
                }
                
                this.currentEstimateHandsId = setTimeout(() => { estimateHands() }, 500)
            };

            estimateHands();
        },
        stopVideoStream() {
            this.$refs.video.srcObject.getTracks().forEach(track => track.stop());
            this.$refs.video.srcObject = null;
        }
    },
};
</script>
