# pfrankov/slicer-copilot

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/pfrankov/slicer-copilot) · 个人维护

**用 LLM 自动调优 Bambu Studio 3D 打印参数的 CLI 工具**

面向 Bambu Studio 用户的 Node.js 命令行工具：读取 .3mf 项目文件中的打印机、耗材与工艺设置，结合用户目标（强度/速度/外观/自定义）调用 OpenAI 兼容 API 的 LLM 生成参数修改建议，并写回新的 .3mf 文件；全程不改动 3D 几何，仅调整工艺设置，且对每项修改给出解释。支持交互/非交互模式、dry-run、六种界面与推理语言、CI/CD 流水线。需 Node.js 20+ 与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 解析 .3mf 归档并让 LLM 按目标调优切片工艺参数
- 只改工艺设置，不修改 3D 几何
- 支持 dry-run 预览、非交互批量模式与 --mock-response 测试
- 六种语言界面与 AI 推理语言切换

## 适用场景

- 按强度/速度/外观等目标一键优化 3D 打印参数
- 在 CI/CD 流水线中批量调优 .3mf 项目
- 打印前用 dry-run 预览参数变更再决定是否应用

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: Slicer Copilot analyzes your `.3mf` project files, understands your goals (like "Maximum Strength" or "Visual Qualit
> L156: 1. **Parses**: Extracts printer info, filament data, and current settings from the `.3mf` archive.
> L158: 3. **Optimizes**: The AI suggests specific setting changes based on your goal.

## 星数曲线

```mermaid
xychart-beta
    title "pfrankov/slicer-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0f2b00eb8601` · [字段定义](../../DATASET.md)*
