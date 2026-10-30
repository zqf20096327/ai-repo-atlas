# jtyszkiew/ImageSmith

⭐ 15 · Python · 推送 2026-02-25 · [GitHub](https://github.com/jtyszkiew/ImageSmith) · 个人维护

**通过 Discord 斜杠命令执行 ComfyUI 工作流的机器人**

面向 Discord 服务器成员的图像/视频/音频生成机器人：将预建的 ComfyUI 工作流映射为斜杠命令（/forge、/reforge、/upscale），注入文本提示或上传图片后在 ComfyUI 实例上执行，自动检测输出类型并回传文件。本产品是工作流执行器而非创建器，工作流需自备。支持多实例负载均衡（LEAST_BUSY/ROUND_ROBIN/RANDOM）、按角色/用户/频道的访问控制、7 种界面语言与 Python 插件扩展。运行依赖外部 ComfyUI 实例与 Discord Bot Token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 斜杠命令映射 ComfyUI 工作流（txt2img/img2img/upscale）
- 多 ComfyUI 实例负载均衡（LEAST_BUSY/ROUND_ROBIN/RANDOM）
- 工作流与设置两级访问控制（角色/用户/频道，AND 组合）
- Python 函数式 settings 与插件/hook 扩展机制

## 适用场景

- 在 Discord 服务器内通过命令生成图像、视频或音频
- 多 ComfyUI 实例间分发生成任务
- 按频道或角色限制成员可用的生成工作流

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L46: ImageSmith exposes slash commands for generating images, videos, and audio from text prompts or existing images. Th
> L11: > **Note**: ImageSmith is a workflow executor, not a workflow creator. You'll need to create your own workflows, bu

## 星数曲线

```mermaid
xychart-beta
    title "jtyszkiew/ImageSmith 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d364b24caf28` · [字段定义](../../DATASET.md)*
