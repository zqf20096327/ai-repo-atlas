# wasabihu/cairnkit

⭐ 3 · Python · MIT · 推送 2026-11-17 · [GitHub](https://github.com/wasabihu/cairnkit) · 个人维护 · 中文 README

**面向业务应用的 agent 运行时：宿主管身份，写入需人工批准**

为多用户业务应用提供的 Python agent 运行时库：身份与权限由宿主应用注入 ToolContext，数据变更通过 propose 访问级别生成草稿，由宿主实现审批后保存。核心机制包括 Hermes Agent 移植的内存快照与写筛查、上下文压缩、prompt 注入扫描、技能管理与委托。核心仅依赖标准库与 httpx，存储与权限留在应用侧；可选 knowledge 模块基于 SQLite 做中英文关键词检索与本地向量检索。示例可离线运行，无需 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 宿主注入 ToolContext 身份，工具分 read/propose/write 三级访问
- propose 草稿 + 宿主审批的写入边界，拒绝则记录不变
- 内存快照、写筛查、档案投影与有界合并的内存机制
- 四阶段上下文压缩与注入扫描（security.py）

## 适用场景

- 在多用户业务后端中让 agent 提议变更并由人审批落库
- 为 agent 会话实现可搜索的内存与历史检索
- 长对话的上下文压缩与 prompt 缓存优化
- 用 ScriptedModel 离线测试 agent 流程

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: **A small agent runtime for business applications.** Give an agent useful tools while
> L43: proposed change becomes a saved record. cairnkit provides building blocks for that:
> L54: - **Small.** The core depends only on the standard library and `httpx`. No web framework,

## 星数曲线

```mermaid
xychart-beta
    title "wasabihu/cairnkit 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `b5e4c33fff76` · [字段定义](../../DATASET.md)*
