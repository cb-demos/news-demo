import { shallowMount } from '@vue/test-utils'
import ListItem from '@/components/ListItem.vue'

describe('ListItem.vue', () => {
  it('renders props.title when passed', () => {
    const title = 'Super popular article'
    const wrapper = shallowMount(ListItem, {
      propsData: { title }
    })
    expect(wrapper.text()).toMatch(title)
  })
  it('renders props.user when passed', () => {
    const user = 'testuser'
    const wrapper = shallowMount(ListItem, {
      propsData: { user }
    })
    expect(wrapper.text()).toMatch(user)
  })
})
