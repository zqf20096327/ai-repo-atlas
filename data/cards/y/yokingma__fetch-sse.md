# yokingma/fetch-sse

⭐ 31 · TypeScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/yokingma/fetch-sse) · 个人维护

**基于 fetch 的 SSE 请求库，供浏览器与 Node.js 消费事件流**

提供 fetchEventData 单一 API 封装 Event Source 请求，保留 Fetch API 的参数传递方式，运行于浏览器与 Node.js（Node 需 v18.0.0 以上）。以 TypeScript 编写，解析 data-only 消息与命名事件两种事件流模式（UTF-8 文本流），支持 skipStatusCheck 选项跳过默认 2xx 状态校验、自行处理响应。旧版浏览器可能需 polyfill TextDecoder。以 npm 包形式分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fetchEventData API，参数传递方式与 Fetch API 一致
- 支持 data-only 与命名事件两种事件流解析
- skipStatusCheck 选项跳过 2xx 状态校验自行处理响应
- TypeScript 编写，兼容浏览器与 Node.js

## 适用场景

- 在前端或 Node 应用中消费 SSE 接口的流式响应
- 处理带命名事件与 id 的事件流协议
- 自定义状态码处理场景下读取事件流

## 场景标签

 · 领域:Web/网络库

## 证据(README 行号)

> L3: This package provides an easy API for making Event Source requests with all the features of Fetch API, and supports 
> L97: this package is written in typescript and compatible with browsers and nodejs, You might need to polyfill TextDecod

## 星数曲线

```mermaid
xychart-beta
    title "yokingma/fetch-sse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `435802fe9ac8` · [字段定义](../../DATASET.md)*
