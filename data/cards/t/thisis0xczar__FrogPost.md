# thisis0xczar/FrogPost

⭐ 108 · JavaScript · 推送 2025-12-04 · [GitHub](https://github.com/thisis0xczar/FrogPost) · 个人维护

**测试 iframe postMessage 通信安全漏洞的 Chrome 扩展**

Chrome 扩展，面向 Web 安全测试人员：实时捕获 iframe 间 postMessage 流量，通过运行时拦截分析消息处理器，检测缺失 origin 校验、危险 DOM sink（innerHTML/eval）、原型污染与 XSS 注入点；支持 Fuzzing、Auto Pilot 自动扫描与 URL 列表批量测试，另识别已注册未收消息的“僵尸”处理器。AI 分析为可选功能：配置 OpenAI/Anthropic/Gemini API key 并运行本地 Node.js 服务器后，可由 LLM 生成 handler 质量评分与定制 payload。基本功能无需服务器与 AI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时捕获并分析 iframe 间 postMessage 流量
- 检测缺失 origin 校验、危险 DOM sink、原型污染等漏洞
- Auto Pilot 自动扫描与 URL 列表批量测试
- 可选 LLM 分析：handler 质量评分与 AI 生成 payload

## 适用场景

- 对自有应用做 postMessage 处理器的 XSS 与原型污染测试
- Bug bounty 中批量扫描多个 URL 的 iframe 通信漏洞
- 持续监控动态加载 iframe 的攻击面

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: FrogPost is a Chrome extension for security testing of `postMessage` communications between iframes. It combines sta
> L49: - **AI Enhancement**: Optional LLM-powered analysis (requires server)
> L93: **Note**: Basic features work without the server, but AI analysis requires it to be running.

## 星数曲线

```mermaid
xychart-beta
    title "thisis0xczar/FrogPost 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-30 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `00c5081a9f58` · [字段定义](../../DATASET.md)*
