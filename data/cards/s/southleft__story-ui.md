# southleft/story-ui

⭐ 237 · TypeScript · MIT · 推送 2026-10-18 · [GitHub](https://github.com/southleft/story-ui) · 个人维护

**嵌入 Storybook 的 AI 界面生成工具：用描述生成真实 story 文件**

在既有 Storybook 项目中增加工作区与面板：用户以自然语言描述界面，工具从项目自身的类型声明、本地源码与 Storybook 索引发现组件，调用 LLM 生成 .stories.tsx 文件，在 Storybook 预览中渲染；每代产物经静态检查与浏览器渲染校验（内容越界/空白/重叠则重新生成），并支持版本历史、diff、点击元素直接改 prop 及一键提交 git 分支。面向产品设计师、设计系统团队与工程师。要求 Storybook 10+、Node 20+、React+TypeScript 设计系统（其他框架用经典面板），需 Anthropic/OpenAI/Gemini 之一的 API key，Playwright 为可选推荐。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从项目类型声明与源码发现组件，prop 与 token 经真实类型校验，模型编造的 token 会被拒绝
- 生成结果为仓库中的 .stories.tsx 文件，可直接提交 PR
- 每代产物经静态检查与 Playwright 浏览器渲染自检，失败则重新生成
- 提供非模型的检查器：点击元素按真实 props 即时改写属性

## 适用场景

- 产品设计师在设计系统内用描述探索完整界面，无需等工程排期
- 设计系统团队让组件被正确组装使用
- 工程师获得已导入正确组件的首稿 story，直接进 PR 流程

## 场景标签

 · 领域:前端/设计系统工具

## 证据(README 行号)

> L8: Story UI adds a workspace to the Storybook you already have. You type what you
> L31: - **The output is real work.** Every generation is a `.stories.tsx` file in
> L84: |**An API key**|Anthropic, OpenAI or Google Gemini. One is enough.|

## 星数曲线

```mermaid
xychart-beta
    title "southleft/story-ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 236 --> 238
    line [237, 237]
```

2026-10-18 237 → 2026-10-23 237（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `17008332421f` · [字段定义](../../DATASET.md)*
