# focuxdot/wokey-provider-node

⭐ 13 · TypeScript · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/focuxdot/wokey-provider-node) · [官网](https://wokey.ai/r/NODE) · 组织维护 · 中文 README

**供 Wokey 平台的共享闲置 AI 订阅流量出口节点**

Wokey 平台的提供方节点软件：用户在本机运行节点，将 Claude/Codex/智谱/Kimi 等 AI 订阅的闲置容量接入 Wokey 平台并按成功路由的调用获得收益。节点通过出站 WebSocket 与平台通信，仅作为受限网络出口转发到厂商官方域名的加密流量，不终止 TLS、不读取提示词，路由/计费/结算均在平台侧。提供本地控制台与 CLI，安装脚本校验 SHA-256，出站域名白名单写入源码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 出站连接白名单硬编码于源码，仅允许厂商官方域名
- 不终止厂商 TLS、不读取提示词与授权头
- 安装器校验 SHA-256 并可选 cosign 签名验证
- 支持 Codex/Claude/Grok 等多种本地授权路径导入

## 适用场景

- 把闲置的 AI 订阅容量接入 Wokey 获取按调用计费收益
- 在自有机器上以出站连接方式运行节点，无需暴露公网端口
- 用 CLI 在无界面 Linux 服务器上完成绑定与授权

## 场景标签

 · 领域:AI 服务基础设施/流量中继

## 证据(README 行号)

> L10: Run a node on your own machine to share idle **Claude / Codex (OpenAI) / Zhipu / Kimi** (and more) subscription cap
> L110: |Wokey Platform|Wokey infrastructure|Accounts, routing, billing, credential custody, vendor request construction, 
> L111: |Provider Node|Your machine|Local console, node binding, credential onboarding, outbound bridge, restricted networ

## 星数曲线

```mermaid
xychart-beta
    title "focuxdot/wokey-provider-node 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-31"]
    y-axis "stars" 9 --> 14
    line [10, 11, 13, 13]
```

2026-10-18 10 → 2026-10-31 13（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `ef6e0c36946d` · [字段定义](../../DATASET.md)*
