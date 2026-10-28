# airblackbox/airblackbox

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/airblackbox/airblackbox) · [官网](https://airblackbox.ai) · 个人维护

**AI agent 飞行记录仪：记录、回放、合规扫描与行为门控**

面向需要对 AI agent 决策留痕问责的开发者的开源基础设施（Apache 2.0），本地运行、代码不出机器。三个功能：以 Ed25519 签名的防篡改链记录 agent 动作（提供 7 个 Python 框架的 trust layer 与 npm 包、覆盖任意语言的网关）；air-blackbox comply 静态扫描代码库并对照欧盟 AI Act 第 9-15 条、GDPR 与美国州法报告缺口，支持 Python/TS/JS/Java/Kotlin/Notebook；covenant 声明 agent 权限并在动作前由 gate 决定。证据可导出为 .air-evidence 文件在浏览器本地验证。限制：网关只记录模型调用而非工具执行；扫描检查项与已知破坏（红队审查 17 处）有记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ed25519 签名 + RFC 3161 外部时间戳锚定的防篡改审计链，可导出浏览器本地验证的 .air-evidence
- 51+ 项检查覆盖 EU AI Act Articles 9-15，映射 ISO 42001/NIST AI RMF/美国州法
- 六种语言（Python/TS/JS/Java/Kotlin/Notebook）同一扫描引擎，等价代码同判定
- OpenAI/Anthropic 兼容网关记录每次模型调用，实测开销约 3ms/次

## 适用场景

- 为生产环境 AI agent 留下第三方可验证的决策证据链
- 扫描代码库生成欧盟 AI Act 合规差距报告
- 在 agent 动作执行前按 covenant 策略做门控拦截
- 事故发生后从审计链回放重建事件过程

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L26: - **Scans.** `air-blackbox comply` reads a codebase and reports gaps against
> L95: The gateway serves the OpenAI chat completions and Responses APIs (forwarded
> L21:  are recorded by trust layers for seven frameworks; TypeScript agents by the

## 星数曲线

```mermaid
xychart-beta
    title "airblackbox/airblackbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f1bd6456922d` · [字段定义](../../DATASET.md)*
