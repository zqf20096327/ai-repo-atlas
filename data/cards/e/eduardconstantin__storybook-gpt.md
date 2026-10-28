# eduardconstantin/storybook-gpt

⭐ 27 · TypeScript · MIT · 推送 2026-02-06 · [GitHub](https://github.com/eduardconstantin/storybook-gpt) · [官网](https://storybook-gpt.vercel.app) · 个人维护

**把 React 组件转换为 Storybook 故事的网页应用**

基于 NextJS 13 构建的 Web 应用，使用 OpenAI API 将用户输入的 React 组件生成为 Storybook story；采用 TypeScript 与 TailwindCSS，支持暗色模式与复制到剪贴板。使用方式为 git clone 克隆源码后 npm install 安装依赖，在 .env 文件配置 OPENAI_API_KEY，npm run dev 启动开发服务器，在浏览器输入组件并点击生成。面向需要为 React 组件编写 Storybook 故事的前端开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 OpenAI API 将 React 组件转换为 Storybook story
- 基于 NextJS 13 + TypeScript + TailwindCSS 构建
- 支持暗色模式与一键复制结果

## 适用场景

- 我为 React 组件快速生成 Storybook 故事初稿
- 我想复制生成的 story 代码到剪贴板使用

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Storybook GPT is a web application that can be used to convert React components into Storybook stories. It is using 
> L44: Add your react component to the input field and hit generate story, in a few seconds you will have a storybook stor

## 星数曲线

```mermaid
xychart-beta
    title "eduardconstantin/storybook-gpt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ace5244475a6` · [字段定义](../../DATASET.md)*
