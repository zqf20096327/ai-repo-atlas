# osim-group/osim-schema

⭐ 37 · Apache-2.0 · 推送 2026-06-17 · [GitHub](https://github.com/osim-group/osim-schema) · [官网](https://www.osim.space/) · 组织维护 · 中文 README

**面向 AI 的开源安全数据标准化 schema 项目，统一安全数据语义层**

OSIM 定义安全数据 schema 语义层，覆盖日志、告警、资产、安全事件四类数据的结构化定义，将异构原始安全数据转化为 AI 可理解的结构化格式，供安全团队、工具与 AI 系统跨数据源进行一致性分析。README 声明的使用场景包括：数据解析为符合 OSIM 标准的 JSON、数据质量校验报告、自然语言转 SQL/ES/SPL 查询、安全场景建设。仓库以 schemas 目录组织定义文件，采用 Apache 2.0 许可证；README 未给出安装命令或运行方式细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义四类安全数据 schema：日志/告警/资产/安全事件
- 使用场景含数据解析为 OSIM 标准 JSON 与数据质量报告
- 自然语言转查询，支持 SQL/ES/SPL 多种格式

## 适用场景

- 把异构安全数据统一为标准化 JSON 供分析
- 校验安全数据质量并获取改进说明
- 用自然语言生成跨 SQL/ES/SPL 的查询语句

## 场景标签

`网络安全` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: OSIM （Open Security Information Model）是 面向 AI 的开源安全数据标准化 项目，通过定义规范统一的安全数据 schema 语义层，破解行业数据碎片化难题，使安全团队、工具和 AI 系统能够在不
> L22: - **标准化：统一安全数据，筑牢流转根基**
> L42: - 日志信息（Log）

## 星数曲线

```mermaid
xychart-beta
    title "osim-group/osim-schema 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-30 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e80df1de58c1` · [字段定义](../../DATASET.md)*
