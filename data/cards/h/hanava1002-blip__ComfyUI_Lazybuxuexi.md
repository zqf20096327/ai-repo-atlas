# hanava1002-blip/ComfyUI_Lazybuxuexi

⭐ 3 · JavaScript · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/hanava1002-blip/ComfyUI_Lazybuxuexi) · [官网](https://space.bilibili.com/3706970246744888) · 个人维护 · 中文 README

**给 ComfyUI 用户提供的视频/音频生成自定义节点包**

Lazy不学习 维护的 ComfyUI 自定义节点集，包含 Wan2.2 Remix 导演台、MinimaxH3 分镜、Krea2/Qwen 图像工作台、YuE 工作台、超分补帧修脸后处理及加载/保存辅助节点，并附带示例工作流 JSON。仓库只含节点代码与工作流，不含模型权重；部分功能需配合已有的模型节点，缺失时运行时提示。通过 ComfyUI Manager 的 Git URL 安装或手动克隆到 custom_nodes，不额外安装 Python 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Wan2.2 Remix、MinimaxH3、Krea2、Qwen2.1、YuE 等模型的导演台与逐段生成节点
- 附带 7 个可直接打开的示例工作流 JSON
- 超分、补帧、二采修脸等成片后处理节点
- 安装不需额外 Python 包，使用 ComfyUI 自带环境

## 适用场景

- 在 ComfyUI 中逐段生成并拼合 Wan 风格视频
- 用 Krea/Qwen 工作台做图像生成与合并
- 对成片做超分、补帧与修脸后处理
- 保存和管理各模型的自定义风格

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: Lazy不学习 的 ComfyUI 自定义节点。装进 `custom_nodes` 后重启即可在节点菜单里看到 `Lazy` 开头的节点。
> L31: 节点本身不额外安装 Python 包，用的是 ComfyUI 自带的环境。部分功能要配合已有的模型节点，例如 MiniMax H3、Wan、Krea2、Qwen、YuE，以及超分 / RIFE 补帧。缺哪个，对应功能会在运行时提示


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `835be6592566` · [字段定义](../../DATASET.md)*
