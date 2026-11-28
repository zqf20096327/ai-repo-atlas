# boitar/sair

⭐ 5 · JavaScript · MIT · 推送 2026-11-08 · [GitHub](https://github.com/boitar/sair) · 个人维护 · 中文 README

**让国行 Apple 智能改用自定义大模型的请求重写插件**

面向 Surge、Loon、Stash、Shadowrocket、Quantumult X 与 Egern 六款 iOS 代理客户端的模块/插件/覆写集合：利用客户端 MITM 与双阶段脚本重写，把国行 Apple 智能（iOS 27.3+）发往通义千问网关的请求转为 OpenAI 兼容的 /v1/chat/completions 调用，并将上游响应重组为 27 级 SSE 事件流喂回系统，覆盖写作工具、Siri 问答与视觉智能三个场景。通过 Safari Web 控制台配置 endpoint、api_key、model 与各场景超时，支持超时/错误时回退官方千问。要求系统仍可访问官方千问通道，且仅支持 OpenAI 兼容上游。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 请求拦截转 OpenAI 协议 + 响应伪造为 27 级 SSE 事件流
- 覆盖写作工具、Siri 问答、视觉智能识图三个原生场景
- Safari Web 控制台配置参数与切换模型服务商预设
- 超时/错误时自动放行官方千问回包的回退机制

## 适用场景

- 让国行版 Apple 智能的写作工具和 Siri 走我自己的 OpenAI/DeepSeek API
- 把视觉智能识图接到支持图片输入的自选模型上
- 在支持的模型超时时自动回退官方千问，避免功能中断

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L30: **SAIR** 本质上是一个面向主流代理客户端的**国行 Apple 智能请求重写与响应适配插件 / 模组**（而非网络层路由器）。
> L33: 1. **请求拦截与协议转接**：捕获 Apple 智能发出的上下文、系统提示词与相机控制多模态图像，转换为标准的 OpenAI `/v1/chat/completions` 请求并转接至你指定的大模型 API；
> L36: 配置启用后，系统级**写作工具**、**Siri 智能问答**和**视觉智能相机**依然保持 100% 的原生系统交互与视觉动效，但底层大模型已完全透明替换为你偏好的 OpenAI、Gemini、Claude、DeepSeek、聚

## 星数曲线

```mermaid
xychart-beta
    title "boitar/sair 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-28"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-10 5 → 2026-11-28 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `6bc3797e3237` · [字段定义](../../DATASET.md)*
