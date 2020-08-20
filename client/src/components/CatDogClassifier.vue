<template>
  <div class="container">
    <div>
      <h2> It's a cat or a dog?</h2>
    </div>
    <section>
      <div class="box">
        <div>
          <img :src="src1" class="img-size" height="300">
        </div>
        <div class="inputWrapper">
          <input class="inputFile" type="file" ref="file" @change="selectFile"/>
        </div>
      </div>
      <div class="box">
        <h3>Upload an Image of a Cat or a Dog so I can predict the result</h3>
        <h4>{{ complement }}</h4>
        <h4>
          {{ predictedAnimal }}
        </h4>
      </div>

    </section>
        <button class="btn btn-success" @click="upload">
          Predict
        </button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import UploadFileService from './../services/UploadFileService';

@Component
export default class CatDogClassifier extends Vue {
  private selectedFiles: any = undefined;
  private currentFile: any = {};
  private src1: any = '';
  private complement: any = ''
  private predictedAnimal: any = '';
  
  selectFile(): void {
    this.selectedFiles = this.$refs.file.files;
    this.currentFile = this.selectedFiles.item(0);
    this.src1 = URL.createObjectURL(this.currentFile)
    console.log(this.currentFile)
  }
  upload() {
      UploadFileService.upload(this.currentFile)
        .then(response => {
          console.log(response);
          // this.animal = response.data.animal;
          this.handlePrediction(response.data)
          this.complement = 'The animal in the image is:'
        });

      this.selectedFiles = undefined;
    }

  handlePrediction(response) {
    if (response.animal === 'dog') {
      this.predictedAnimal = 'a Dog';
    } else {
      this.predictedAnimal = 'a Cat';
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  margin-top: 100px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.img-size {
  max-width: 300px;
}
section {
  justify-content: center;
  display: flex;
  flex-wrap: wrap;
}
.inputWrapper {
  display: block;
  margin: 15px;
  justify-content: center;
}
.fileInput {
  justify-content: center;
}
input {
  justify-content: center;
}
button {

  background-color: #333;
}
.box {
  margin: 20px 50px;
  flex-wrap: wrap;
  width: 300px;
}

.inputFile {
  overflow: hidden;
  display: block;
  position: relative;
  width: 100px;
  margin: auto;
  cursor: pointer;
  border: 0;
  height: 30px;
  border-radius: 5px;
  outline: 0;
}
.inputFile:hover:after {
  background: #333;
}
.inputFile:after {
  transition: 200ms all ease;
  border-bottom: 3px solid rgba(0,0,0,.2);
  background: #333;
  text-shadow: 0 2px 0 rgba(0,0,0,.2);
  color: #fff;
  font-size: 14px;
  text-align: center;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: block;
  content: 'Upload Image';
  line-height: 30px;
  border-radius: 5px;
}
button {
  overflow: hidden;
  display: block;
  position: relative;
  width: 200px;
  margin: auto;
  cursor: pointer;
  font-size: 20px;
  border: 0;
  height: 60px;
  border-radius: 5px;
  color: #fff;
  outline: 0;

}
button {
  overflow: hidden;
  display: block;
  position: relative;
  width: 200px;
  margin: auto;
  cursor: pointer;
  font-size: 20px;
  border: 0;
  height: 60px;
  border-radius: 5px;
  color: #fff;
  outline: 0;

}

button :after {
  transition: 200ms all ease;
  border-bottom: 3px solid rgba(0,0,0,.2);
  background: #333;
  text-shadow: 0 2px 0 rgba(0,0,0,.2);
  color: #fff;
  font-size: 20px;
  text-align: center;

}
</style>
