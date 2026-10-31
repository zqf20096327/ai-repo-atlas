# Rjxshr1/idea-to-print

⭐ 17 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Rjxshr1/idea-to-print) · 个人维护 · 中文 README

**Agent 技能集：从文字或图片生成可打印的 3D 雕塑并完成切片交付**

面向具备图像与文件工具的 Agent 宿主（如 Claude 类技能目录）的 3 个可安装技能与配套 Python 工具，串联图像生成、腾讯混元 3.1 官方 SDK 图生 3D、Blender 模型处理与 Bambu Studio 离线切片。提供统一执行账本管理阶段、尝试与证据，内置 16 项几何检查（自相交、壁厚、底面接触、重心稳定性），全部通过才标记 print_ready。混元 API 需腾讯云凭据与额度；Blender 与 Bambu Studio 需单独安装；打印机发送仅经官方界面，配套脚本只做只读状态查询。

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

- 混元 3.1 官方 SDK 适配器，支持主图与补充视角、按打印尺寸选面数（上限 150 万）
- 统一执行账本（next/status/record/reconcile/export）管理与恢复各阶段版本与证据
- 几何可打印性检查（自相交、壁厚、底面接触面积、重心稳定性），PASS/FAIL/UNKNOWN 三态门控
- 离线 demo 脚本：无需账号、网络或打印机跑通全流程并生成 3D 转台/AR 预览页

## 适用场景

- 我说一句话或给一张参考图，让 Agent 生成可打印的手办雕塑并交付切片包
- 检查已有 STL 的可打印性并完成指定打印机/耗材的切片预览
- 给 3D 打印作业留全流程证据与版本，交付时附六视图、关键层截图与文件清单

## 场景标签

 · 领域:3D 建模/3D 打印

## 证据(README 行号)

> L7: 项目包含 **3 个可安装的 Agent 技能和配套 Python 工具**，串联图像生成、混元 3D、Blender 和 Bambu Studio。支持宠物、神兽等有机雕塑，也能从已有 STL/BLEND 开始处理。Agent 根
> L40: 在具备图像、建模和文件工具的 Agent 中：
> L65: 将 `--destination` 改为 Agent 实际使用的技能目录，例如 `~/.codex/skills`。目标已有同名技能时，安装器会停止并保留现有内容；新安装会记录当前 Python 的绝对路径。更新已有安装时，合并技

## 星数曲线

```mermaid
xychart-beta
    title "Rjxshr1/idea-to-print 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a8f373923533` · [字段定义](../../DATASET.md)*
