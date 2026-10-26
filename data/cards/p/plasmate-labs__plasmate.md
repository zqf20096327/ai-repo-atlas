# plasmate-labs/plasmate

⭐ 38 · Rust · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/plasmate-labs/plasmate) · [官网](https://docs.plasmate.app) · 组织维护

**面向 AI agent 的浏览器引擎：输入 HTML，输出结构化语义对象模型**

用 Rust 编写的浏览器引擎，将 HTML 编译为结构化的 Semantic Object Model（SOM）JSON，去除展示与运行时标记，供 LLM 直接推理。内嵌 V8 运行 JavaScript，实现受支持的 CDP 子集以兼容 Puppeteer 工作流。原生提供 MCP 工具服务器（约 25 个工具，含抓取、抽取、截图、有状态页面交互、cookie、动作追踪与回放校验）与 AWP v0.1 协议（7 个线方法及网络拦截、代理池等扩展），另有带确认审批的有状态工作流执行与 RFC 9309 robots.txt 爬取策略评估。页面 JavaScript 默认关闭，渲染运行于沙箱。限制：SOM 输出尺寸随页面/配置/分词器变化；不做视觉模型图像理解。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HTML 编译为结构化 SOM JSON，去除展示与运行时标记
- 原生 MCP 与 AWP 协议，实现文档化 CDP 子集兼容 Puppeteer
- 内嵌 V8 运行 JavaScript，页面 JS 默认关闭且渲染沙箱化
- 有状态工作流需逐步 --confirm-step 审批，动作追踪仅内存留存、可验证回放

## 适用场景

- 为 LLM/agent 管线提供网页的结构化输入，替代原始 HTML
- 通过 MCP 接入 Claude Desktop/Cursor 等客户端做网页抓取与交互
- 用 Puppeteer 脚本连接 CDP 服务器运行既有自动化工作流
- 爬取前评估 RFC 9309 robots.txt 爬取策略

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L24: Plasmate compiles HTML into a **Semantic Object Model (SOM)**, a structured
> L105: ### Run as an MCP tool server (Model Context Protocol)
> L166: Plasmate is purpose-built for AI agent pipelines. Several ways to wire it in:

## 星数曲线

```mermaid
xychart-beta
    title "plasmate-labs/plasmate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f5c7dcfe2b33` · [字段定义](../../DATASET.md)*
