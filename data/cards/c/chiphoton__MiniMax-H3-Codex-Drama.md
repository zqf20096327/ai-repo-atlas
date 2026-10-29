# chiphoton/MiniMax-H3-Codex-Drama

⭐ 61 · JavaScript · MIT · 推送 2026-09-28 · [GitHub](https://github.com/chiphoton/MiniMax-H3-Codex-Drama) · 个人维护 · 中文 README

**在 Codex 内把故事/剧本做成成片的 MiniMax H3 视频生产插件**

面向 Codex 的视频与原生音频生产插件，以 marketplace 安装，含十个技能的生产插件、h3style 官方技能伴包、privacy 本地媒体工具和 canvas 网页工作流引擎四部分。Codex 负责规划生产：从 brief 建立角色/场景事实源、分镜，将每个镜头路由到对应的 MiniMax H3 工作流（T2V/I2V/R2V/纯音频），通过本地 ComfyUI（comfyui-mcp@0.49.3）提交并监控生成，再用 FFmpeg 做剪辑、混音、字幕与 QC，全程可断点续跑。默认启用 H3 Turbo LoRA（6 步），不静默下载模型或安装节点，需自备 Node.js、ComfyUI 与 MiniMax H3 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- brief→角色/场景设定→分镜→关键帧→镜头→成片的完整生产链，含跨镜头一致性追踪
- 通过本地 ComfyUI 运行 MiniMax H3 官方工作流，支持 T2V/I2V/R2V 与纯音频生成
- 默认 H3 Turbo LoRA 6 步生成，可用 [turbo=false] 回到 20 步原工作流
- privacy 插件提供不查看内容的本地压缩/切片/元数据清理工具

## 适用场景

- 把剧本或品牌 brief 交由 Codex 规划并生成完整多镜头短片
- 从本地参考视频提炼可复用的风格 profile 用于后续制作
- 在本地 ComfyUI 上以参考图控制角色身份与镜头运动生成单镜头
- 对隐私敏感的本地视频做内容盲处理（压缩、切片、去元数据）

## 场景标签

`视频生成` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L15: MiniMax-H3 Drama is a **Codex-first video and native-audio production plugin**, not just a prompt collection. Codex
> L142: |⚙️|`minimax-h3-comfyui`|Prepare, validate, submit, monitor, and fetch local H3 workflows|

## 星数曲线

```mermaid
xychart-beta
    title "chiphoton/MiniMax-H3-Codex-Drama 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-29"]
    y-axis "stars" 58 --> 62
    line [59, 60, 61, 61]
```

2026-10-18 59 → 2026-10-29 61（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `73ea077987d1` · [字段定义](../../DATASET.md)*
