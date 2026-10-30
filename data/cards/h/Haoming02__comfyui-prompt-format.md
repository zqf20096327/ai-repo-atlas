# Haoming02/comfyui-prompt-format

⭐ 36 · JavaScript · MIT · 推送 2025-11-19 · [GitHub](https://github.com/Haoming02/comfyui-prompt-format) · 个人维护

**ComfyUI 扩展：清理与格式化提示词文本**

一个 ComfyUI 扩展，在菜单中添加 Format 按钮，对提示词文本做清理：移除多余空格与逗号、修正错位的括号与逗号、可选去重相同标签（仅适用于标签式提示词，句子式不生效）、可选将下划线替换为空格、保留换行并在换行处追加逗号，支持 Alt+Shift+F 快捷键手动触发。面向使用 ComfyUI 生成 Stable Diffusion 图像、需要整理提示词的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 移除多余空格与逗号、修正错位括号
- 标签去重（仅限标签式提示词，按行检查）
- 下划线替换为空格（可选）
- Alt+Shift+F 快捷键触发格式化

## 适用场景

- 整理标签式提示词中的重复标签与多余符号
- 批量修正提示词中的括号与逗号位置

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L2: This is an Extension for ComfyUI, which helps formatting texts.
> L5: This adds a button, **Format**, to the menu which when clicked will:

## 星数曲线

```mermaid
xychart-beta
    title "Haoming02/comfyui-prompt-format 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-30 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fdf3cb694fdb` · [字段定义](../../DATASET.md)*
