<template>
    <div>
      <!--<comment :id="$route.params.id"></comment>-->
      <comment :id=1></comment>123
    </div>
</template>

<script>
import comment from '../subcomponents/comment'
export default {
  name: 'GoodsComment',
  components: {
    comment
  }
}
</script>
