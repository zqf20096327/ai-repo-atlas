# VoidEclipseAI/ReFrameVideo

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/VoidEclipseAI/ReFrameVideo) · 个人维护 · 中文 README

**开源视频分层编辑工具：改画面元素后由 AI 重生成整段视频**

面向视频创作者的开源工具包，含两部分：视频编辑器用 SAM 3.1 把视频中的人物与物体切成图层，可移动、缩放、翻转、隐藏或删改画幅，操作方式类似 Photoshop；ReFrameVideo LoRA 基于 MiniMax H3 训练，根据编辑生成的粗剪、逐帧遮罩与首帧参考图重生成整段视频并填补空缺。模型运行依赖 ComfyUI（本地或远程），也可接入云 API；所有模型输入与 workflow_api.json 可导出，长视频分段编辑。后端无鉴权仅限本地浏览器使用，完整测试仅覆盖 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- SAM 3.1 主体检测，将视频元素转为可编辑图层（可选 MatAnyone2 软边缘）
- MiniMax H3 + 自训练 LoRA 依粗剪、遮罩、首帧三类输入重生成视频
- 可接入自有 ComfyUI 工作流或云 API，支持导出全部模型输入与 workflow_api.json
- 支持长视频分段编辑与版本/操作历史

## 适用场景

- 把视频里的人物或物体移动、缩放或删除后重新生成画面
- 修改视频画幅（如 16:9 转 1:1）并补全新增区域
- 用参考首帧控制最终镜头的画面效果
- 在自己已有的 ComfyUI 工作流中复用导出的输入与 workflow

## 场景标签

`微调` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L13: ReFrameVideo is an open-source personal project that lets you freely change the picture of an existing video. Move,
> L15: - **A video editor**: uses SAM 3.1 to turn the elements of a video into layers that you edit freely, as in Photosho
> L16: - **The ReFrameVideo LoRA**: trained on MiniMax H3, it regenerates the whole clip from your edit and fills in the g


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `72765bb2aa9c` · [字段定义](../../DATASET.md)*
