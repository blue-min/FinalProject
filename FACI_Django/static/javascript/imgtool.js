/*
  (function () {
        var webglBackend;
        try {
          webglBackend = new fabric.WebglFilterBackend();
        } catch (e) {
          console.log(e)
        }
        var canvas2dBackend = new fabric.Canvas2dFilterBackend()

        fabric.filterBackend = fabric.initFilterBackend();
        fabric.Object.prototype.transparentCorners = false;
        var $ = function (img) { return document.getElementById(img) };

        function applyFilter(index, filter) {
          var obj = canvas.getActiveObject();
          obj.filters[index] = filter;
          var timeStart = +new Date();
          obj.applyFilters();
          var timeEnd = +new Date();
          var dimString = canvas.getActiveObject().width + ' x ' +
            canvas.getActiveObject().height;
          $('bench').innerHTML = dimString + 'px ' +
            parseFloat(timeEnd - timeStart) + 'ms';
          canvas.renderAll();
        }

        function getFilter(index) {
          var obj = canvas.getActiveObject();
          return obj.filters[index];
        }

        function applyFilterValue(index, prop, value) {
          var obj = canvas.getActiveObject();
          if (obj.filters[index]) {
            obj.filters[index][prop] = value;
            var timeStart = +new Date();
            obj.applyFilters();
            var timeEnd = +new Date();
            var dimString = canvas.getActiveObject().width + ' x ' +
              canvas.getActiveObject().height;
            $('bench').innerHTML = dimString + 'px ' +
              parseFloat(timeEnd - timeStart) + 'ms';
            canvas.renderAll();
          }
        }

        fabric.Object.prototype.padding = 5;
        fabric.Object.prototype.transparentCorners = false;

        var canvas = this.__canvas = new fabric.Canvas('c'),
          f = fabric.Image.filters;

        canvas.on({
          'selection:created': function () {
            fabric.util.toArray(document.getElementsByTagName('input'))
              .forEach(function (el) { el.disabled = false; })

            var filters = ['grayscale',
              'blend-color',
              'resize'];


          },
          'selection:cleared': function () {
            fabric.util.toArray(document.getElementsByTagName('input'))
              .forEach(function (el) { el.disabled = true; })
          }
        });


        fabric.Image.fromURL("{% static 'images/result.svg' %}", function (img) {
          var oImg = img.set({ left: 150, top: 0 }).scale(0.4);
          canvas.add(oImg);
        });



        for (var i = 0; i < 10; i++) {
          console.log(i,$('icon'+(i+1)))
          $('icon' + (i + 1)).addEventListener('click', function () {
            // console.log(this.id)
            fabric.Image.fromURL("{% static 'images/result'" + this.id + "'.svg' %}", function (img) {
              var oImg = img.set({ left: 0, top: 270 }).scale(0.2);
              canvas.add(oImg);
            });
          })

        };

        $('remove_img').addEventListener('click', function () {
            console.log("안녕")
              if(canvas.getActiveObject().cacheKey != 'texture1'){
                canvas.remove(canvas.getActiveObject());
              }

          });





        // 텍스트 추가하는 js 시작
        $('draw_text').addEventListener('click', function(){
          var textbox = new fabric.Textbox('Text', {
          fill: 'red'
          // left: 50,
          // top: 50,
          // width: 150,
          // fontSize: 20

        });
       canvas.add(textbox).setActiveObject(textbox);
        });
        // 텍스트 추가하는 js 끝




        $('webgl').onclick = function () {
          if (this.checked) {
            fabric.filterBackend = webglBackend;
          } else {
            fabric.filterBackend = canvas2dBackend;
          }
        };

        $('grayscale').onclick = function () {
          applyFilter(0, this.checked && new f.Grayscale());
        };

        $('blend').onclick = function () {
          applyFilter(16, this.checked && new f.BlendColor({


            color: document.getElementById('blend-color').value,
            mode: document.getElementById('blend-mode').value,
            alpha: document.getElementById('blend-alpha').value
          }));
        };



        $('blend-alpha').oninput = function () {
          applyFilterValue(16, 'alpha', this.value);
        };


        $('save_img').onclick = function () {
          const image = canvas.toDataURL();
          const link = document.createElement("a");
          link.href = image;
          link.download = "logo";
          link.click();
        };




      })();

      // 캔버스 이미지 업로드  js

      var canvas = new fabric.Canvas('c');
      var imgElement = document.getElementById('img');
      var imgInstance = new fabric.Image(imgElement, {
        left: 100,
        top: 100,
        angle: 30,
        opacity: 0.85
      });
      canvas.add(imgInstance);
*/
