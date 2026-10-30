# Poll-The-People/customgpt-starter-kit

⭐ 53 · TypeScript · 推送 2026-10-10 · [GitHub](https://github.com/Poll-The-People/customgpt-starter-kit) · [官网](https://customgpt.ai/starterkit) · 组织维护

**CustomGPT.ai RAG API 的聊天界面启动套件（小组件/独立应用）**

基于 Next.js 的聊天前端，接入 CustomGPT.ai 的 RAG API：支持 iframe 嵌入、直接小组件、浮动按钮与独立应用四种部署形态，提供服务端 API 代理与密钥管理、实时流式响应、文件上传、引用展示与语音输入（语音需 OpenAI API key）。附带完整 Docker 与 Vercel 部署选项、CDN 即贴即用脚本及 React/原生 JS 集成示例。使用者需自备 CustomGPT.ai 的 API key 与 agent ID。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种部署形态：iframe 嵌入、直接小组件、浮动按钮、独立应用
- 服务端 API 代理，密钥仅存于服务端环境变量，不暴露给浏览器
- CDN 脚本 30 秒接入任意网站，无需构建过程
- 文件上传、引用展示、语音输入（语音需 OpenAI API key）

## 适用场景

- 把 CustomGPT.ai 的 agent 以聊天小组件嵌入自己的网站
- 自托管一个可定制主题与品牌的企业聊天界面
- 快速演示自建 CustomGPT.ai agent 的对话与引用效果

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3:  A modern, secure chat interface for CustomGPT.ai's RAG API with multiple deployment options including embedded widg
> L67: - 🚀 **Multiple Deployment Modes**: Iframe embed, direct widget, floating button, or standalone
> L85: - **Proxy API Routes**: All API calls go through Next.js API routes that add authentication

## 星数曲线

```mermaid
xychart-beta
    title "Poll-The-People/customgpt-starter-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-30 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `008c6ba57b15` · [字段定义](../../DATASET.md)*
