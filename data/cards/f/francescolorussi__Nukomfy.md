# francescolorussi/Nukomfy

⭐ 35 · Python · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/francescolorussi/Nukomfy) · 个人维护

**把 ComfyUI 工作流封装为 Nuke gizmo 的 Foundry Nuke 插件**

Foundry Nuke 的 Python 插件：将 ComfyUI 工作流转换为可复用的 Nuke gizmo，TD 在 ComfyUI App Builder 与 Workflow Creator 中把工作流控件暴露为 gizmo 旋钮；艺术家在合成内连接素材、设置参数后提交任务到网络中的 ComfyUI 机器，Render Manager 通过 websocket 实时显示进度，完成后可回导帧并保留任务历史。需要 Nuke 14.1+、ComfyUI HTTP 可达、每台机器安装 ComfyUI-Nukomfy-Suite 及共享文件夹；官方仅支持图像序列输入输出，处于早期开发阶段。在 Windows 和 Linux 上测试过，macOS 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ComfyUI 工作流转换为带自动生成旋钮的 Nuke gizmo
- 任务提交到网络内 ComfyUI 机器，Render Manager 实时进度监控与队列管理
- 任务历史保留日志，ComfyUI 重启后仍可回导帧
- 依赖 ComfyUI-Nukomfy-Suite 提供 NukomfyRead/NukomfyWrite 节点在 Nuke 与 ComfyUI 间传递帧

## 适用场景

- VFX 团队把 ComfyUI 工作流分发给合成师，在 Nuke 内直接调用
- 在网络内多台 ComfyUI 机器上渲染图像序列并回导入合成
- 管理团队共享的工作流库与渲染队列

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: **Nukomfy** is a Python plugin for **Foundry Nuke** that lets you turn **ComfyUI** workflows into reusable Nuke gizm
> L20: 1. **Configure a gizmo.** Turn a ComfyUI workflow into a Nuke gizmo. Expose its widgets in ComfyUI's App Builder, c
> L22: 3. **Submit.** Connect your plates, set the knobs, and send the job to a ComfyUI machine. Nukomfy applies your pre-

## 星数曲线

```mermaid
xychart-beta
    title "francescolorussi/Nukomfy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-26 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6a07fd0618a7` · [字段定义](../../DATASET.md)*
