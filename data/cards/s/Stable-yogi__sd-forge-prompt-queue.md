# Stable-yogi/sd-forge-prompt-queue

⭐ 3 · JavaScript · MIT · 推送 2026-11-06 · [GitHub](https://github.com/Stable-yogi/sd-forge-prompt-queue) · 个人维护

**为 Forge Neo 提供多任务生成排队的 WebUI 扩展**

SD WebUI Forge Neo 的队列扩展：在 Generate 旁一键捕获当前页面全部设置（提示词、尺寸、种子、采样器、hires fix 及其他扩展选项）加入队列，任务后台依次运行。支持批量 ×N、暂停/恢复、停止当前任务、拖拽重排、逐任务撤销、完成后重跑或回填设置，队列跨页面刷新与 Forge 重启持久化，并暴露无鉴权的 HTTP JSON API。经 URL 安装或 clone 到 extensions/ 目录，在 Forge Neo 2.29 与 neo-2.30.1 上测试通过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 捕获页面全部设置入队，txt2img/img2img 均支持，×N 批量时每份独立种子
- 队列面板：暂停/恢复、停止、拖拽重排、移除带 Undo、完成 job 回填设置
- 队列跨页面刷新与 Forge 重启持久化，重启后等待任务自动继续
- 完整 HTTP JSON API（状态/暂停/移动/重跑/取图等路由）

## 适用场景

- 连续排队多组参数的图像生成而无需逐次等待
- 整理失败或需重跑的任务，按优先级调整执行顺序
- 通过 API 程序化查看与操控生成队列

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L48: Extensions tab → Install from URL → paste this repository's URL → Install,
> L53: - Forge Neo **2.29** (`neo` branch, commit 8a6bc1d), in daily use since October 2026.

## 星数曲线

```mermaid
xychart-beta
    title "Stable-yogi/sd-forge-prompt-queue 星数(近 2 点)"
    x-axis ["2026-11-11", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-11 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `d018e0cfe1ef` · [字段定义](../../DATASET.md)*
