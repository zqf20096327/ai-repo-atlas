# f/gutenwright

⭐ 26 · PHP · 推送 2026-08-20 · [GitHub](https://github.com/f/gutenwright) · [官网](https://playground.wordpress.net/?blueprint-url=https://raw.githubusercontent.com/f/gutenwright/main/blueprint.json) · 个人维护

**自然语言生成 Gutenberg 区块的 WordPress 插件**

实验性 WordPress 插件：在区块编辑器中读取当前文章上下文，将自然语言提示流式发送给后端 AI 模型，产出序列化 Gutenberg 区块（HTML/SVG、表格、组织架构图、沙箱交互组件、AI 生成图片入库）。后端要求模型输出严格 JSON，区块插入前经解析、白名单与净化；脚本内容隔离在无同源访问的 iframe 沙箱中。API key 仅服务端存储，支持 WordPress 7.0 Connectors 或自定义密钥。项目声明为实验性，发布前需人工审阅生成内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 上下文感知生成：发送受限文章上下文使区块匹配当前文章
- 流式编辑器反馈并返回真实序列化 Gutenberg 区块
- 脚本/样式内容隔离在无同源访问的沙箱区块
- 可选 OpenAI Images 生成图片并导入媒体库

## 适用场景

- 在 WordPress 编辑器里用一句话生成对比表格、SVG 架构图
- 为文章生成交互式小组件（游戏、计算器）并安全沙箱渲染
- 生成排版图片并自动插入媒体库与文章

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L22: Gutenwright is an experimental WordPress plugin that turns natural language prompts into real Gutenberg blocks. It 
> L44: - **Optional image generation**: Generates images with OpenAI Images, imports them into the Media Library, and inse

## 星数曲线

```mermaid
xychart-beta
    title "f/gutenwright 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `37675783a27f` · [字段定义](../../DATASET.md)*
