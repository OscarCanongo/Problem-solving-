function songDecoder(song){
  console.log(song);
  const regex = /WUB/g;
  song = song.replace(regex, ' ');
  song = song.replace(/^\s+|\s+$|\s+(?=\s)/g, "");
  console.log(song);
  return song;
}