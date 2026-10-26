# ryannli/tiny-roommate

⭐ 45 · JavaScript · 推送 2026-03-30 · [GitHub](https://github.com/ryannli/tiny-roommate) · 个人维护

**住在 macOS 桌面上的 AI 宠物猫，能看屏幕、陪伴、记日记**

基于 Tauri v2 构建的桌面 AI 陪伴宠物：一只（或六种可选角色的）小动物常驻桌面，走动、打盹、偶尔弹出与环境相关的对话气泡。机制上通过屏幕截取读取用户当前活动，交由用户选择的 Claude Code 或 Gemini CLI 充当 AI 大脑，产生情境化反应；长期记忆以纯 Markdown 文件存于 .pet-data/，全程本地运行，数据不出机器。仅支持 macOS（Windows/Linux 在路线图），需 Node.js v18+、Rust，首次运行需编译 Rust；无 AI CLI 时宠物仍可运行但不会思考或说话。角色可通过自定义精灵图扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 屏幕感知：截屏后由 Claude Code 或 Gemini CLI 生成情境化反应
- 持久记忆以纯 Markdown 文件本地存储（日记/主人记忆/时间线）
- 6 个内置角色，支持自定义精灵图扩展
- 无 AI CLI 时仍可运行为纯桌面宠物

## 适用场景

- 长时间编程时想要一个桌面陪伴小动物
- 让宠物根据我的屏幕活动做出相关反应或提醒休息
- 阅读宠物的 Markdown 日记查看每日活动记录

## 场景标签

 · 领域:桌面应用/AI 陪伴

## 证据(README 行号)

> L18: **It sees what you see**
> L19: Screen capture + your chosen AI CLI — knows if you're coding, designing, or doom-scrolling.
> L33: **100% local**

## 星数曲线

```mermaid
xychart-beta
    title "ryannli/tiny-roommate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8784ac0d7919` · [字段定义](../../DATASET.md)*
