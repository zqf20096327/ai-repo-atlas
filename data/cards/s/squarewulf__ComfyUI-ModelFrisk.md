# squarewulf/ComfyUI-ModelFrisk

⭐ 10 · JavaScript · 推送 2025-12-21 · [GitHub](https://github.com/squarewulf/ComfyUI-ModelFrisk) · 个人维护

**ComfyUI 插件：自动检测并修复工作流缺失的模型路径**

一个 ComfyUI 自定义节点插件，扫描已加载工作流中因模型缺失而报错的节点（红节点），并提供三种修复方式：路径精确匹配（如模型被移动到子文件夹时自动更新路径）、模糊匹配（文件名相似时弹出 Near Match 选择对话框供用户确认）、一键批量修复全部缺失模型。通过 git clone 安装到 ComfyUI/custom_nodes/ 目录，重启后从右键菜单调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描工作流中模型缺失节点（红节点）
- 精确匹配：模型移动到其他文件夹时自动更新路径
- 模糊匹配：相似文件名弹出 Near Match 选择对话框
- 一键批量修复全部缺失模型

## 适用场景

- 从他人分享的工作流加载后模型路径对不上本机目录
- 整理模型目录（如移入 flux 子文件夹）后批量修复路径
- 文件名有拼写差异时通过近匹配找到正确模型

## 场景标签

 · 领域:AI 图像生成工具/ComfyUI 生态

## 证据(README 行号)

> L3: A custom node/plugin for ComfyUI that automatically detects and fixes missing model paths in your workflow.
> L7: - **Auto-Location**: Scans your loaded workflow for nodes with missing models (red nodes).

## 星数曲线

```mermaid
xychart-beta
    title "squarewulf/ComfyUI-ModelFrisk 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-26 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `bccfb46b4629` · [字段定义](../../DATASET.md)*
