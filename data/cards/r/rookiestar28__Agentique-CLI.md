# rookiestar28/Agentique-CLI

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-07-04 · [GitHub](https://github.com/rookiestar28/Agentique-CLI) · [官网](https://www.agentique.io) · 组织维护

**AI agent 资源平台的配套开发套件：schema、本地校验与只读回读**

Agentique.io 平台的公共配套开发者套件，面向资源创作者与集成者：提供公开 JSON Schema 契约、静态 starter 包、无执行的本地包校验 CLI 与库、最小权限 GitHub Action 校验包装、只读公共 API 回读客户端，以及仅限审查的上传准备 CLI。本地工具不发布、不安装、不执行资源；最终发布由平台持有并经账户/token 门控。协调包集以 npm 发布于 0.2.2 版本，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无执行的本地校验 CLI 与库（manifest、路径、哈希、类密内容检查）
- 最小权限 GitHub Action 包装本地校验
- 只读回读客户端与徽章助手，查询公共目录/信任/下载元数据
- 仅在元数据、POST 票据、文件名、字节数与 SHA-256 校验通过后才下载产物字节

## 适用场景

- 在提交给平台前本地准备并校验 agent/skill/workflow 资源包
- 集成方查询公共 Agentique 目录与资源状态
- 在 CI 中以只读 Action 运行资源包校验

## 场景标签

 · 领域:AI agent 生态/资源分发

## 证据(README 行号)

> L9: This repository is the public companion developer kit for Agentique creators and integrators. It provides public sch
> L7: Agentique.io is a platform for preparing, reviewing, publishing, and displaying public AI resource listings. The pla

## 星数曲线

```mermaid
xychart-beta
    title "rookiestar28/Agentique-CLI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7487171c6513` · [字段定义](../../DATASET.md)*
