<template>
    <div>
      <comment :id="$route.params.id"></comment>
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
