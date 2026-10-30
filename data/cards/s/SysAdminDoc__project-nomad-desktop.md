# SysAdminDoc/project-nomad-desktop

⭐ 16 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/SysAdminDoc/project-nomad-desktop) · [官网](https://github.com/SysAdminDoc/project-nomad-desktop/releases/latest) · 个人维护

**离线优先的个人应急备灾桌面工作台，可选本地 AI 助手**

面向个人与家庭的备灾与野外作业桌面应用：以就绪度评分、物资清单与消耗率规划、离线地图（PMTiles/GPX）、Kiwix 离线知识库、检查表、事件日志与可打印报告为核心，数据以 SQLite 本地存储，无账号、无遥测、默认绑定 localhost。可安装并管理 Ollama、Qdrant、Kiwix 等可选本地服务，连接 Ollama 提供私有本地助手，对话与索引文档留在本机。Windows 提供安装包与便携版，Linux/macOS 需从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 就绪度评分覆盖水、食品、医疗、通信等七类并指向薄弱记录
- 物资消耗率计算剩余天数与采购缺口
- 离线地图（区域包下载/PMTiles 导入/GPX 导出）与 Kiwix ZIM 图书馆管理
- 可选安装管理 Ollama/Qdrant 等本地服务，私有助手数据留存本机

## 适用场景

- 断网前把地图、参考库和应急记录下载到一台机器上
- 跟踪家庭物资库存、保质期与消耗节奏
- 离线查阅维基百科类 ZIM 库并生成可打印的状态报告
- 在本地硬件条件允许时接入 Ollama 做私有问答

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L18: NOMAD turns scattered spreadsheets, bookmarks, and emergency notes into one private field desk. Track supplies. Mea
> L41: - Add a private local assistant with Ollama when your hardware and use case call for it.
> L54: |**Local assistant**|Connects to Ollama and optional Qdrant collections. Conversations and indexed documents remain

## 星数曲线

```mermaid
xychart-beta
    title "SysAdminDoc/project-nomad-desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d58c360ea32e` · [字段定义](../../DATASET.md)*
