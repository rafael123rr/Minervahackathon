import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpEventType} from '@angular/common/http';
import {  FileUploader, FileSelectDirective } from 'ng2-file-upload/ng2-file-upload';
const URL = 'http://127.0.0.1:4996/img';
@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html',
  styleUrls: ['./image-upload.component.scss']
})
export class ImageUploadComponent implements OnInit {

  
 
  constructor(private http: HttpClient) { }

  public uploader: FileUploader = new FileUploader({url: URL, itemAlias: 'photo'});
  

  ngOnInit() {
    
    this.uploader.onAfterAddingFile = (file) => { file.withCredentials = false; };
    console.log(File.name);
    this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
         console.log('ImageUpload:uploaded:', item, status, response);
         alert('File uploaded successfully');
     };

  }
}
