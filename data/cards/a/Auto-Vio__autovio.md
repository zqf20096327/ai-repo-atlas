# Auto-Vio/autovio

⭐ 33 · TypeScript · NOASSERTION · 推送 2026-04-12 · [GitHub](https://github.com/Auto-Vio/autovio) · [官网](https://auto-vio.github.io/autovio-docs/) · 组织维护

**开源端到端 AI 视频生成流水线：文本提示生成 MP4**

面向 SaaS 团队与开发者的自托管 AI 视频生成流水线：文本提示经 LLM 生成分镜脚本，Gemini/DALL-E 3 生成图像，Veo/Runway 将图像动画化为视频片段，最终在时间线编辑器中合成并导出 MP4。各角色（LLM/视觉分析/图像/视频）可按项目混搭不同提供商，自带 API key 运行在自己基础设施上。提供 REST API 与 OpenAPI 文档，并附带含 25+ 工具的 MCP 服务器供 Claude Code、Cursor 等 AI 客户端调用。技术栈为 TypeScript/React/Express/MongoDB，需 Bun 或 Node.js、MongoDB 与 FFmpeg。许可为 PolyForm Noncommercial 1.0.0（非商业）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五步流水线：初始化→参考视频分析→LLM 分镜脚本→图像与视频生成→时间线编辑导出
- 多提供商混搭：LLM（Gemini/OpenAI/Claude）、图像（Gemini Image/DALL-E 3）、视频（Veo/Runway）
- 完整 MCP 服务器（25+ 工具），可从 Claude Code/Cursor/Claude Desktop 调用
- REST API + OpenAPI，全部功能可编程访问

## 适用场景

- 把功能规格自动转化为 SaaS 产品演示视频
- 通过 Claude Code/Cursor 在编辑器内直接生成产品演示视频
- 接入 n8n/Make/Zapier 或 CI/CD，按部署事件自动生成发布宣传视频
- 用项目风格指南批量产出保持品牌一致性的多语言视频变体

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L26: You describe what you want — a product, an idea, a story. AutoVio writes the scene-by-scene scenario, generates an 
> L31: Text prompt  →  Scenario (LLM)  →  Images (Gemini / DALL-E)  →  Video clips (Veo / Runway)  →  Edit  →  Export
> L42: |**3 · Scenario**|LLM writes a scene-by-scene script with image prompts, video prompts, and transitions|
> L43: |**4 · Generate**|Each scene gets an AI-generated image, then that image is animated into a video clip|

## 星数曲线

```mermaid
xychart-beta
    title "Auto-Vio/autovio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-28 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3a4614c6a5d9` · [字段定义](../../DATASET.md)*
