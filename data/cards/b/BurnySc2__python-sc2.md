# BurnySc2/python-sc2

⭐ 638 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/BurnySc2/python-sc2) · 个人维护

**用 Python 3 编写星际争霸 II AI 机器人的客户端库**

封装星际争霸 II 脚本 API 的 Python 客户端库（BurnySc2 维护的 Dentosal 仓库 fork），提供高、低两层抽象，目标是用少于二十行代码实现 worker rush 机器人。仅覆盖 raw scripted 接口，不计划支持图形界面接口。运行需本机 StarCraft II 可执行文件与地图文件，支持 Windows/macOS 安装版、Linux（Wine/Lutris/无头二进制）与 WSL 环境。以 pypi 包（burnysc2）分发，随库附带 protoss/terran/zerg 各族示例机器人。fork 与主仓库不兼容共存，需虚拟环境隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供高低两层抽象，简单 bot 可控制在二十行内
- 支持 Linux（Wine/Lutris）与 WSL 环境运行
- 提供 API 配置项：距离计算方法（scipy pdist/cdist）、game_step 帧控制等
- examples/ 目录包含各族示例机器人

## 适用场景

- 编写星际争霸 II 对战 AI 机器人并本地运行
- 参加 SC2 AI Arena 天梯对战
- 学习通过脚本 API 与星际争霸 II 引擎交互

## 场景标签

 · 领域:游戏/AI bot 开发

## 证据(README 行号)

> L6: An easy-to-use library for writing AI Bots for StarCraft II in Python 3. The ultimate goal is simplicity and ease of
> L8: **This library (currently) covers only the raw scripted interface.** At this time I don't intend to add support for 

## 星数曲线

```mermaid
xychart-beta
    title "BurnySc2/python-sc2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 637 --> 639
    line [638, 638]
```

2026-10-18 638 → 2026-10-26 638（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `bacb62d1560b` · [字段定义](../../DATASET.md)*
