# ShieldNet-360/secure-vibe

⭐ 23 · Go · MIT · 推送 2026-08-14 · [GitHub](https://github.com/ShieldNet-360/secure-vibe) · 组织维护

**给 AI 编码助手的签名安全技能库与确定性 CI 安全门禁**

面向使用 AI 编码助手和 CI 流水线的开发/DevOps 团队：单个静态 Go 二进制同时充当 CLI、CI 门禁和 MCP 服务器（20 个工具）。在代码生成时向 8 种助手注入 33 个 Ed25519 签名的 SKILL.md 安全知识；检测侧用四类确定性扫描器（密钥、依赖/CVE/OSV、Dockerfile、GitHub Actions）审计代码树或 PR diff，支持 SARIF 输出与严重度门禁。离线、无需 API key、不调用 LLM；动态验证交给编码 agent 通过 MCP 原语完成。自称窄域设计，非通用 SAST。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 33 个签名技能嵌入 8 种 AI 编码助手（生成时防护）
- 单一 Go 二进制 = CLI + CI 门禁 + MCP 服务器（20 个工具）
- 四类确定性扫描器：密钥/依赖恶意库与 CVE/Dockerfile/GitHub Actions
- 离线、无 key、无遥测，Ed25519 签名发布

## 适用场景

- 让 Claude Code/Cursor/Copilot 等助手在写代码时遵循安全规范
- 在 CI 中对 PR diff 做安全审计并按严重度阻断构建
- 查询某个 npm/PyPI 包是否为恶意或 typosquat 包

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9: assistant signed `SKILL.md` security knowledge *at the point of code generation*,
> L11: `secure-vibe` — is **both** the CLI/gate **and** the MCP server. Offline, keyless,
> L80: the *reasoning* and *dynamic verification* are your coding agent's job, so the

## 星数曲线

```mermaid
xychart-beta
    title "ShieldNet-360/secure-vibe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f74fc4731586` · [字段定义](../../DATASET.md)*
