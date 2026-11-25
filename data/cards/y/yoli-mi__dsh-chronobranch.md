# yoli-mi/dsh-chronobranch

⭐ 6 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/yoli-mi/dsh-chronobranch) · 个人维护 · 中文 README

**DSH 会话的时间线分支画布插件：可视化分叉与多对话关联**

面向 DeepSeek Harness (DSH) 的原生插件，以「时间线」视图标签挂载到会话顶部，提供点线泳道时间轴画布：支持三档缩放与全文检索、原地展开 Markdown 对话卡片、调用 DSH 原生 sessions.fork 实现共用底部输入框的分支、同工作区多对话关联成共享时间线组、微观执行小轴（推理/工具调用/Diff）、屏幕磁贴与 Windows 桌面悬浮卡片。提供桌面端内一键安装、源码挂载与 dsh CLI 三种安装方式，需 DSH Desktop 0.2.2+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性点线泳道排版，L1 鸟瞰 / L2 点线 / L3 展开三档缩放与全文检索
- 复用 DSH 底部唯一输入框的分叉体验，保留模型选择、附件、斜杠命令与审批流
- 同工作区任意多段对话关联为共享时间线组（支持传递合并）
- 7 个快捷键注册进 DSH 原生设置，支持磁吸磁贴与 Windows 桌面悬浮卡片

## 适用场景

- 在长对话中从任意轮次分叉探索不同方案
- 将同一工作区多个对话串联到一条时间线查看
- 把关键轮次悬挂为屏幕磁贴边聊边对照

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: **ChronoBranch** 是面向 **DeepSeek Harness (DSH)** 的原生横向点线时空分支画布插件。
> L10: 它直接以原生视图标签 **`时间线`** 挂载在 DSH 会话顶部的 `对话` / `轨迹` 旁，自动跟随 DSH 浅色与深色主题，将长对话、分叉探索、同工作区多对话关联、Agent 执行轨迹与自由悬浮磁贴统一在一个克制清晰的点线
> L21: - **不再引入第二套输入框**：在任意已完成轮次点击「分叉」，立即调用 DSH 原生 `sessions.fork({ sessionId, atSeq, increaseTitle: true })` 并通过 `uiWorks

## 星数曲线

```mermaid
xychart-beta
    title "yoli-mi/dsh-chronobranch 星数(近 3 点)"
    x-axis ["2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 2 --> 7
    line [3, 5, 6]
```

2026-11-22 3 → 2026-11-25 6（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `32190ec9ab66` · [字段定义](../../DATASET.md)*
