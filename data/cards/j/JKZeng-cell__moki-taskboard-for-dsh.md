# JKZeng-cell/moki-taskboard-for-dsh

⭐ 3 · JavaScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/JKZeng-cell/moki-taskboard-for-dsh) · 个人维护 · 中文 README

**为 DeepSeek Harness Desktop 提供项目看板与 agent 任务调度插件**

MOKI 是 DeepSeek Harness Desktop 的插件，在桌面端添加项目任务台：从聊天中捕获请求并匹配为项目任务、把任务派发到 DSH 会话执行、以看板/表格/活动视图管理任务，并保存带版本管理的附件与交付物。审核流程含自动检查与人工批准/退回，支持选择主机与模型处理会话。数据库与托管文件本地存储；语义捕获与会话调度需宿主运行并消耗所选模型账户额度。Windows 平台以 tgz 插件包分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从聊天语义匹配捕获请求并生成关联任务
- 任务派发到 DSH 会话并产出带版本的交付物
- 交付审核含自动检查与批准/退回流程
- 数据库与托管文件本地存储

## 适用场景

- 把编辑器聊天中的需求转为项目任务卡片
- 用看板跟踪多个项目的任务进度与周活动
- 审核 agent 交付物并记录批准或退回决定
- 在本地管理任务附件的多个版本

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: MOKI adds a project taskboard to DeepSeek Harness Desktop. Track requests from chats, dispatch tasks to DSH sessions
> L98: Reopen DSH and select MOKI Taskboard for DSH in the sidebar. Files open in the right-hand preview. Approval notific

## 星数曲线

```mermaid
xychart-beta
    title "JKZeng-cell/moki-taskboard-for-dsh 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `400e95444c66` · [字段定义](../../DATASET.md)*
