# microsoft/cates

⭐ 15 · TypeScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/microsoft/cates) · 组织维护

**编码智能体配置的静态评分器：检测 token 效率与安全合规**

Coding Agent Token Economics Standard (CATES) 的参考实现，来自 Microsoft。对仓库指令、prompt 库、聊天模式、MCP 配置、hooks 等编码智能体配置面做零 LLM 调用的静态分析：49 条稳定规则覆盖 token 效率、安全、完整性等 6 个维度，输出文本/JSON/SARIF 报告并支持 CI 门禁（min-score、require-level 等）。附带 cates-optimize 应用无损修复、托管 HTTP 服务（粘贴/扫描 GitHub URL）、Docker 镜像与 Helm chart。初始扫描为配置评估而非成本证明，经济性评估为独立的实验性功能。需 Node.js >= 22.12，首个版本尚未发布，需源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 零 LLM 调用的确定性静态分析，无需 API key
- 49 条稳定规则、6 个评分维度，可按规则/维度开关并输出 SARIF
- CI 门禁（--min-score/--require-level/--fail-on）与安全自动修复 --fix
- 同一引擎覆盖 CLI、npm、Docker、Helm 与托管 HTTP 服务

## 适用场景

- 在 CI 中给编码智能体配置设 token 效率与安全门禁
- 审查仓库的 agent 指令与 MCP 配置是否符合 CATES Level 1/2/3
- 批量扫描多仓库生成配置合规汇总报告

## 场景标签

 · 领域:开发者工具/AI 工程治理

## 证据(README 行号)

> L3: > Score coding-agent configurations for **token efficiency**, **security**, and **CATES conformance** — zero LLM cal
> L5: This is the reference implementation for the **Coding Agent Token Economics Standard (CATES)**. It is vendor-neutral

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/cates 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `daca1817f0b1` · [字段定义](../../DATASET.md)*
