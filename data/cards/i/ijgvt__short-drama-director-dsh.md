# ijgvt/short-drama-director-dsh

⭐ 3 · JavaScript · NOASSERTION · 推送 2026-11-05 · [GitHub](https://github.com/ijgvt/short-drama-director-dsh) · 个人维护 · 中文 README

**面向短剧创作者的 DSH 插件：剧本到分镜、提示词与 ComfyUI 生成**

一个 DeepSeek Harness / DSH Desktop 插件，把短剧制作流程放进创作台：从剧本盘点人物/场景/道具资产，生成分镜与视频提示词并绑定资产版本，转换为 MiniMax H3 中文格式，再提交到本机或云端 ComfyUI 执行生成，负责任务提交、结果回收与归档。支持本地/云端双端工作流配置、工作流能力扫描与兼容性预检。运行要求 DSH Desktop（peer 0.2.0-rc.2）与 ComfyUI 实例；Windows 为本地实例启停与桌面安装的完整支持平台。许可为源码公开许可，非 OSI 开源，禁止二次售卖插件本体。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 剧本→资产→分镜→视频提示词→H3 格式的流程整合
- 支持本地/云端 ComfyUI 双端配置与切换
- 自动扫描工作流目录，识别能力、模型引用与输出节点状态
- 插件随附已验证工作流与 ComfyUI 整合包公开下载

## 适用场景

- 不想手动连 ComfyUI 节点的单人短剧创作者
- 需要项目交接、资产复用与逐镜头重做的小团队
- 用本地 ComfyUI 替代按张付费生图 API 做图片视频生成

## 场景标签

`工作流自动化` `图像生成` `视频生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: > 想用 ComfyUI 免费做短剧，又不想学节点连线？这个项目把剧本、资产、分镜、视频提示词和 H3 工作流放进了 DeepSeek Harness 的创作台。
> L5: 短剧制作导演是一个 **DeepSeek Harness / DSH Desktop 插件**，不是 DeepSeek 网页版功能，也不是通用 Agent 插件。它通过 Agent 调用本机或云端 ComfyUI，并在插件内提供资产
> L7: 它适合不想从零搭 ComfyUI 工作流的单人创作者，也适合需要交接项目、复用资产和逐步返工的小团队。默认目标是让用户判断内容，插件负责资产绑定、工作流选择、任务提交、结果回收和归档。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9edd58fe5d86` · [字段定义](../../DATASET.md)*
