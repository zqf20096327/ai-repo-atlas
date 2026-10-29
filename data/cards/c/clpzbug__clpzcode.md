# clpzbug/clpzcode

⭐ 18 · TypeScript · NOASSERTION · 推送 2026-06-05 · [GitHub](https://github.com/clpzbug/clpzcode) · 个人维护

**面向渗透测试者的 AI 编码 agent CLI：一个目标跑完攻击链**

基于 Claude Code 分叉的终端 AI agent，面向渗透测试与 bug bounty 用户提供自动化攻击管线：输入一个目标 URL 后由 agent 依次执行子域枚举、端点发现、指纹识别、漏洞检测、利用与提权链，直至输出报告。支持多 agent 并行（不同模型分别跑侦察/利用/AD 枚举），内置 29 条提权链与 /exploit、/ad、/chain 等命令。模型接入支持 xAI Grok、OpenAI、本地 Ollama、GitHub Models、Gemini 及任意 OpenAI 兼容端点；需 Bun≥1.1 或 Node.js≥18，npm 安装。仅限授权测试目标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI agent 读取每步工具结果并决定下一步动作（如 SQLi 500 后转时间盲注、SSTI 验证后升格 RCE）
- 29 条内置提权链（SSRF→云元数据→IAM 窃取、SQLi→OS shell→提权、ADCS ESC1→DA 证书→DCSync 等）
- 多 agent 并行：不同模型的子 agent 同时执行侦察/利用/AD 枚举
- 多提供商接入：xAI、OpenAI、Ollama、GitHub Models、Gemini 及 OpenAI 兼容端点，会话中 /model 切换

## 适用场景

- 授权测试中对一个 Web 目标跑完整渗透管线并出 findings 报告
- 活动目录环境给定 DC IP 与域名后自动跑 AD 攻击管线
- bug bounty 场景下让 agent 链式利用多个已确认漏洞

## 场景标签

`网络安全` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L27: **It thinks, not just runs.**
> L37: Not locked to one API. Run on xAI Grok, local Ollama models, OpenAI, GitHub Models, Gemini, or any OpenAI-compatibl
> L136: Built for bug bounty hunters and security researchers.

## 星数曲线

```mermaid
xychart-beta
    title "clpzbug/clpzcode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3af888f96735` · [字段定义](../../DATASET.md)*
