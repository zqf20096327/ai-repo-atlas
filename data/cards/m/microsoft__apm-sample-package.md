# microsoft/apm-sample-package

⭐ 18 · MIT · 推送 2026-05-05 · [GitHub](https://github.com/microsoft/apm-sample-package) · 组织维护

**APM 示例包：演示 instructions/prompts/skills/agents 四类原语**

微软发布的 Agent Package Manager（APM）示例包，演示 APM 包的全部四种原语类型：instructions（设计规范编码标准）、prompts（设计评审、无障碍审计）、skills（样式检查）、agents（设计评审专家角色）。包内声明对 github/awesome-copilot/skills/review-and-refactor 的传递依赖，安装时由 APM 自动解析。定位为开发者创建自有 APM 包时的参考模板，需通过 apm 命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 APM 全部四种原语类型的示例文件
- 声明传递依赖并由 APM 自动解析
- 作为创建自定义 APM 包的参考模板

## 适用场景

- 学习 APM 包结构与各原语类型的写法
- 作为自建 APM 包的起步模板
- 验证 apm install 的依赖解析流程

## 场景标签

 · 领域:AI 开发者工具/Agent 包管理

## 证据(README 行号)

> L3: A sample APM package demonstrating all primitive types: instructions, prompts, skills, and agents.
> L10: apm install microsoft/apm-sample-package

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/apm-sample-package 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2c756fba2df9` · [字段定义](../../DATASET.md)*
