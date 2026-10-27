# jangtrinh/design-os-3d-blender

⭐ 104 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/jangtrinh/design-os-3d-blender) · [官网](https://jangtrinh.github.io/design-os-3d-blender/) · 个人维护

**供 AI 编码代理调用的 Blender 参数化 3D 机械零件生成技能**

以 Claude Code 插件/Codex/Gemini CLI 等编码代理技能（SKILL.md）形式分发，驱动 Blender 的 Python API（bpy）与 Three.js：从英文描述或 JSON 参数生成齿轮、外壳、机架与爆炸装配体，导出 glTF/STL 等格式，并附带交互式浏览器 CAD 查看器页面。产出经确定性验证门（非流形边检查、包围盒尺寸校验、self_check.py）。声明零遥测、100% 本地执行；许可证为 PolyForm Shield 1.0.0，禁止转售或构建竞争产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从英文/JSON 参数生成参数化 bpy 零件脚本并导出 glTF/STL
- 生成自带 Three.js 交互 CAD 查看器的单文件 HTML
- 确定性验证门：非流形边、包围盒、self_check.py 校验
- 声明零遥测、全本地执行（PRIVACY.md 审计）

## 适用场景

- 让编码代理按规格生成可 3D 打印的机械零件并导出 STL
- 为零件搭建可爆炸视图交互的浏览器 CAD 展示页
- 对导出网格做拓扑与尺寸容差审计

## 场景标签

 · 领域:3D/CAD 生成工具

## 证据(README 行号)

> L168: 1. **Intent Routing** — Your AI agent matches your request against `skills/design-os-3d-blender/SKILL.md` frontmat
> L79: Choose the setup that matches your AI coding agent. Every option installs the same canonical skill (`skills/design-

## 星数曲线

```mermaid
xychart-beta
    title "jangtrinh/design-os-3d-blender 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 95 --> 105
    line [96, 102, 104]
```

2026-10-18 96 → 2026-10-27 104（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a2e263859112` · [字段定义](../../DATASET.md)*
