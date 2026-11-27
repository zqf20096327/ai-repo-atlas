# CesiumGS/cesiumjs-ai-starter-app

⭐ 10 · TypeScript · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/CesiumGS/cesiumjs-ai-starter-app) · [官网](https://cesiumgs.github.io/cesiumjs-ai-starter-app/) · 组织维护

**给开发者的 CesiumJS 3D 地球 + LLM 工具调用入门模板**

可运行的起步模板：CesiumJS 三维地球搭配 LLM 聊天面板，模型通过结构化工具调用（flyTo、实体、影像等）驱动地球；复杂请求经 executeCesiumCode 工具走人工审批→后端 AST 校验→浏览器 QuickJS-WASM 沙箱执行的流程，generateCzml 工具生成并校验 CZML 文档。推理全部在后端 Node.js API 完成，API key 不进入浏览器。支持 OpenAI/Anthropic/Google 三家 provider，可选接入 MCP 客户端桥与浏览器 WebMCP，提供 Docker 与本地开发两种启动方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 通过工具调用驱动 3D 地球（flyTo、实体、影像、CZML 等）
- 生成代码经后端 AST 校验 + 前端 QuickJS-WASM 沙箱隔离执行，并默认人工审批
- LLM API key 不进入浏览器，推理在后端 Node.js API 完成
- 支持 MCP 客户端桥（OAuth 自动检测、审批门控）与浏览器 WebMCP 标准注册

## 适用场景

- 作为起点开发自己的 LLM 驱动三维地球应用
- 为已有 CesiumJS 场景接入自然语言控制与代码生成
- 学习 LLM 工具调用、代码沙箱与 MCP 接入的工程实现

## 场景标签

`代码生成` `教程课程` · 领域:编码与开发

## 证据(README 行号)

> L5: A ready-to-run starter pairing a CesiumJS 3D globe with an LLM-powered chat interface. The LLM drives the globe thro
> L11: You need an **LLM API key** from OpenAI, Anthropic, or Google Generative AI to enable chat. A free Cesium Ion token
> L49: For requests that don't fit a single tool call, try something like **`add 3D buildings and fly over New York`**. Th

## 星数曲线

```mermaid
xychart-beta
    title "CesiumGS/cesiumjs-ai-starter-app 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `529c64db2122` · [字段定义](../../DATASET.md)*
