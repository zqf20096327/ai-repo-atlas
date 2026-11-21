# Mannan-Goyal/omp-sidelight

⭐ 5 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/Mannan-Goyal/omp-sidelight) · [官网](https://www.npmjs.com/package/omp-sidelight) · 个人维护

**omp 编码 agent 长回答的全屏阅读与侧栏追问插件**

omp（oh-my-pi）的插件，把编码 agent 生成的长回答渲染成全屏文档页面，支持表格与图示渲染、大纲、搜索与进度条。用户可选中任意段落按键提问，回答流式输出到侧栏线程；侧问通过 side-turn API 进行，不写入主会话上下文。文档版本标记变更块，存储在会话文件夹内。需要 omp 18.11 及以上版本的交互式 TUI，110 列以下单栏显示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选中段落后在侧栏线程提问，不进入主会话上下文
- 全屏渲染表格与图示，带大纲、搜索与变更标记
- omp plugin install 一条命令安装，含两分钟引导教程
- 侧问数据仅存本地会话文件夹

## 适用场景

- 阅读 agent 输出的长篇解释而非滚动聊天记录
- 针对回答中某个具体段落追问而不打断主任务
- 跟踪文档被 agent 修改后的变化部分

## 场景标签

 · 领域:开发者工具/编码 agent 辅助

## 证据(README 行号)

> L14: **Sidelight gives long answers a proper page, and lets you question any line of it on the side.** It's a plugin for
> L17: - **Ask about exactly the part you don't get.** Select a sentence and press a key. The answer arrives in a side thr
> L139: - **Side threads never enter the conversation.** They use omp's side-turn API (`ctx.runEphemeralTurn`, the same on

## 星数曲线

```mermaid
xychart-beta
    title "Mannan-Goyal/omp-sidelight 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-19", "2026-11-21"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-21 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `07c134c04e21` · [字段定义](../../DATASET.md)*
