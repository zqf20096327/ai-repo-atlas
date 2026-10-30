# sonuoffsec/DVAP

⭐ 30 · TypeScript · NOASSERTION · 推送 2026-06-10 · [GitHub](https://github.com/sonuoffsec/DVAP) · 个人维护

**本地自托管 AI 安全训练与测试平台：含漏洞靶场、CTF 与基准**

面向安全专业人员、AI 工程师与研究者的开源 AI 安全平台，提供 15 个容器化的故意脆弱 AI 环境（提示注入、RAG 投毒、MCP 安全、多智能体攻击等），每个实验带 flag、提示与 OWASP LLM Top 10 及 MITRE ATLAS 映射。含 CTF 挑战、对本地模型的攻击套件评测引擎、研究工作区（记录 prompt、记忆、工具调用与 agent 行为）及报告生成。全栈通过 Docker Compose 部署，LLM 推理依赖 Ollama，各实验容器网络隔离、实例 1 小时 TTL 自动停止。已知取舍：API 容器挂载 docker.sock 获得 root 级权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个容器化漏洞实验，映射 OWASP LLM Top 10 与 MITRE ATLAS
- 本地 LLM 安全基准评测（提示注入/越狱/数据外泄套件）
- 研究工作区记录 prompt、记忆、工具调用与攻击链全轨迹
- Findings Dashboard 输出带严重度与导出报告的安全发现

## 适用场景

- 安全研究者本地练习提示注入、RAG 投毒等 AI 攻击
- 红蓝队演练与 AI 安全 CTF 培训
- 对本地模型跑安全基准并生成 OWASP/CVSS 映射报告

## 场景标签

`网络安全` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L37: DVAP is an open-source AI security research, training, benchmarking, and red teaming platform designed to help secu
> L91: Evaluate local and external models against AI security attack suites.
> L178: Each lab runs in an isolated Docker container with its own Ollama-backed LLM endpoint.

## 星数曲线

```mermaid
xychart-beta
    title "sonuoffsec/DVAP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `5fc84198e206` · [字段定义](../../DATASET.md)*
