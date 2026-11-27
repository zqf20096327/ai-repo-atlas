# Rambotx/fine-grained-pose-controllable-human-image-synthesis

⭐ 3 · Python · NOASSERTION · 推送 2026-11-12 · [GitHub](https://github.com/Rambotx/fine-grained-pose-controllable-human-image-synthesis) · 个人维护 · 中文 README

**拖拽骨架微调姿态并用 ControlNet+SD1.5 重新生成人体图像**

课程/大学生创新训练项目的工程原型：从照片用 OpenposeDetector 提取 OpenPose 骨架，注入自研 HTML Canvas 编辑器，用户拖拽 18 个关节点后通过 POST /api/pose 回传，由 ControlNet OpenPose + Stable Diffusion 1.5 按新姿态生成图像。提供一体化 Gradio、FastAPI 前后端分离、纯离线编辑器、独立骨架提取四种运行方式；支持任意 SD1.5 系底模与懒加载。限制：Python 3.13 不支持、仅身体 18 点可编辑、单人/低分辨率、无鉴权且默认只监听 127.0.0.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 检测到的关键点直接注入编辑器，可从真实姿态微调而非从 T-pose 摆起
- 编辑器导出经 /api/pose 自动回传后端，无需下载再上传
- CPU offload + fp16 使 8 GB 显存可运行，模型懒加载
- 提供一体化 Gradio / FastAPI 分离 / 纯离线编辑器 / 骨架提取四种形态

## 适用场景

- 上传人物照片后拖拽骨架摆出新动作并生成对应图像
- 只提取 OpenPose 骨架供其他 ControlNet 工作流使用
- 为控制人物姿态替代纯提示词的文生图尝试

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L18: 文生图模型很难用一句 prompt 精确控制人物姿态。本项目把「姿态」从提示词里拿出来，变成一个**可拖拽的骨架**：
> L22: 3. **回传 + 生成** —— 点「导出并回传」，骨架通过 `POST /api/pose` 直接交给后端，再点「开始生成」，ControlNet（`lllyasviel/control_v11p_sd15_openpose`
> L179: 一页完成「上传原图 → 提取骨架 → 编辑器微调 → 导出并回传 → 生成」，编辑结果自动回传，适合演示。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2ce1bc7f8015` · [字段定义](../../DATASET.md)*
