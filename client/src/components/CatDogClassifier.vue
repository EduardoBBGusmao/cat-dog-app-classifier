<template>
  <div class="width-50 h-100 d-flex justify-content-center">
    <div class=" d-flex"> 
      <div class="flex-col-sm  align-self-center max-w">
        <div>
          <div class="app-title">CAT OR DOG CLASSIFIER</div>
        </div>
        <section>
          <div class="app-description">
           Find out if it’s a cat or a dog! It’s very simple, just upload a photo and then I will predict the result!
          </div>
          <div class="box">
            <div class="input-group">
              <div class="custom-file">
                <input type="file" ref="file" @change="selectFile" class="custom-file-input" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04">
                <label class="custom-file-label" for="inputGroupFile04">{{currentFile.name}}</label>
              </div>
            </div>
          </div>
          <div class="predict-response">
            {{ predictedAnimal }}
            </div>
        </section>
        <button class="btn btn-predict" @click="upload">
          Predict
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import UploadFileService from './../services/UploadFileService';

@Component
export default class CatDogClassifier extends Vue {
  private selectedFiles: any = undefined;
  private currentFile: any = {name:'Choose File'};
  private src1: any = '';
  private complement: any = ''
  private predictedAnimal: any = '';
  
  selectFile(): void {
    this.selectedFiles = this.$refs.file.files;
    this.currentFile = this.selectedFiles.item(0);
    this.src1 = URL.createObjectURL(this.currentFile)
    this.predictedAnimal = '';
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
      const dogProb = Math.round(parseFloat(response.dog_prob)*100);
      this.predictedAnimal = `${dogProb}% probability of being a Dog`;
    } else {
      const catProb = Math.round(parseFloat(response.cat_prob)*100);
      this.predictedAnimal = `${catProb}% probability of being a Cat`;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
.max-w {
  max-width: 480px;
  text-align: justify;
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
h2 {
  margin: 0;
  padding: 0;
}
input {
  justify-content: center;
}
button {

  background-color: #333;
}
.box {
  padding: 20px 50px;
  margin: 20px 0;
  flex-wrap: wrap;
  width: 300px;
}

.app-title {
  font-style: normal;
  font-weight: 900;
  font-size: 70px;
  line-height: 78px;
  margin-bottom: 30px;
  color: #5C5CCC;

}
  .width-50 {
    width: 50%;
  }
@media screen and (max-width: 600px)  {
  .width-50 {
    width: 100%;
    padding: 30px;
  }
  .app-title {
    font-style: normal;
    font-weight: 900;
    font-size: 40px;
    line-height: 50px;
    margin-bottom: 30px;
    color: #5C5CCC;
  }
}
.app-description {
  text-align: justify;
  font-size: 26px;
  line-height: 30px;

  color: #000000;
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
.predict-response {
  font-size: 20px;
  margin-bottom: 40px;
}

.btn-predict {
  background-color: #5C5CCC;
  width: 100%;
  color: white;
}

.btn-predict :hover {
  color: black;
  background-color: white;
}
</style>
