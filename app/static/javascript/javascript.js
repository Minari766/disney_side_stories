let intervalId;
let image = document.getElementById('targetImage');
image.onclick = changeImage;

function changeImage(){

  if(image.style.opacity == ''){
    image.style.opacity = 1;
  }

  let opacityInt = image.style.opacity * 100;
  //フェードアウトの処理（opacityを100ミリ秒ごとに0.1づつ減らす）
  let intervalId = setInterval( () => {
    opacityInt = opacityInt - 10;
    image.style.opacity = opacityInt / 100;

    if(image.style.opacity <= 0){
      clearInterval(intervalId);
      //画像を交換
      if(image.src === 'https://picsum.photos/id/1080/200'){
        image.src = 'https://picsum.photos/id/1039/200';
      }else{
        image.src = 'https://picsum.photos/id/1080/200';
      }

      opacityInt = image.style.opacity * 100;
      //フェードインの処理（opacityを100ミリ秒ごとに0.1づつ増やす）
      intervalId = setInterval( () => {
        opacityInt = opacityInt + 10;
        image.style.opacity = opacityInt / 100;
        if(image.style.opacity >= 1){
          clearInterval(intervalId);
        }
      }, 100);
    }
  }, 100);
}