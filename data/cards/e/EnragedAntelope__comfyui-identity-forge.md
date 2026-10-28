# EnragedAntelope/comfyui-identity-forge

⭐ 28 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/EnragedAntelope/comfyui-identity-forge) · 个人维护

**ComfyUI 角色生成节点组：下拉菜单生成连贯可复现的角色提示词**

一组 ComfyUI 自定义节点，把菜单选择转换为自然语言角色描述，输出 prompt_text、prompt_json 与 subject_text。核心节点 Identity Forge 提供可锁定/随机的下拉字段与约束引擎（如室内不出现露天光照、肤色与血统匹配）；另有 Cosplayer（带手工校对服装描述的虚构角色扮演）、Creature、Archetype、Modifier、Turnaround（一次队列输出多视角）、Expression Sheet（多表情）与 Vault 存取节点。种子驱动可复现，但 2.0.0 起同一种子在版本间不再产出相同角色，需用 Vault 保存。安装方式为克隆到 custom_nodes，无 Python 依赖。

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

- 约束引擎自动消除字段间矛盾，产出连贯的种子可复现角色
- Cosplayer 节点为每个角色提供手工校对的服装描述，不依赖模型是否认识该角色
- Turnaround/Expression Sheet 节点一次队列输出同一角色的多视角/多表情提示词列表
- 预设节点通过 upstream 输入链式堆叠，冲突时最靠近 Identity Forge 的节点生效

## 适用场景

- 不写提示词、只用下拉菜单生成连贯的虚构人物
- 生成漫画/动画角色设定表（多视角参考图）
- 在文生图工作流中复现同一角色用于系列创作
- 以角色扮演（cosplay）形式渲染知名虚构角色

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: Identity Forge turns menu choices into clean, natural-language character descriptions that feed directly into your i
> L86: |**Identity Forge**|Lockable dropdowns in collapsible groups + the constraint engine → `prompt_text` (prose), `prom

## 星数曲线

```mermaid
xychart-beta
    title "EnragedAntelope/comfyui-identity-forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2a5773669a76` · [字段定义](../../DATASET.md)*
