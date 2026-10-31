# jeffy5/comfyui-faceless-node

⭐ 62 · Python · 推送 2026-04-03 · [GitHub](https://github.com/jeffy5/comfyui-faceless-node) · 个人维护

**ComfyUI 换脸节点：图像/视频换脸与修复，基于 facefusion**

面向 ComfyUI 用户的人脸工具自定义节点，基于 FaceFusion 实现图像与视频的换脸及人脸修复功能。安装方式为克隆到 custom_nodes 目录并安装依赖，需手动下载或用脚本下载模型文件到 ComfyUI/models/faceless。提供图像换脸修复、视频换脸修复、视频帧预览三个示例工作流；视频预览暂不支持，输出保存到 output/faceless 目录。项目声明仍在开发中，未来升级可能有兼容性问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 图像与视频的换脸与人脸修复工作流
- 基于 FaceFusion 实现，模型与 facefusion assets 相同
- 提供 download_models.py 脚本下载默认或全部模型

## 适用场景

- 在 ComfyUI 中对图像进行换脸与人脸修复
- 对视频执行换脸与修复处理
- 浏览示例工作流了解节点用法

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L1: # Faceless Node for ComfyUI
> L78: Thanks to Facefusion. This project is based on facefusion to implenment a special version for ComfyUI.

## 星数曲线

```mermaid
xychart-beta
    title "jeffy5/comfyui-faceless-node 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-31 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3878d21950d8` · [字段定义](../../DATASET.md)*
