# AtlasOmnia/community-plugins

⭐ 54 · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/AtlasOmnia/community-plugins) · [官网](https://hermesagenttools.com/) · 组织维护

**Hermes 桌面客户端社区插件策展清单（仅列举、未经审计）**

由 AtlasOmnia 维护的策展列表，收录面向 Hermes Agent（Nous Research）桌面客户端的社区插件条目，按外观、协作工作流、机器人与远程控制、会话洞察、模型基础设施、任务笔记等类别组织。每个条目链接到独立维护的插件仓库，README 明确声明条目经核验存在可加载的 plugin.js，但'仅列举、未经安全审计'。插件的机制为单个 ESM JavaScript 文件，放入 ~/.hermes/desktop-plugins/ 目录即被桌面应用热加载，部分插件可选 Python 后端。通过 PR 提交新条目，要求仓库公开、说明真实功能且无混淆代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 12+ 类别组织的插件条目表，每条链接独立仓库与作者
- 插件形态为单个 ESM plugin.js，目录放置即被桌面应用热加载
- 收录要求：可加载 @hermes/plugin-sdk、公开仓库、无混淆代码与凭据收集
- 声明条目经存在性核验但非安全审计

## 适用场景

- 为 Hermes 桌面客户端寻找外观主题或界面扩展插件
- 查找会话成本、配额、状态监控类插件
- 按提交要求将自己的插件加入清单

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L7: A curated list of community-made plugins for the Hermes desktop client, maintained by AtlasOmnia.
> L36: Every entry below was verified against a public repository containing a native Hermes Desktop `plugin.js` that impo

## 星数曲线

```mermaid
xychart-beta
    title "AtlasOmnia/community-plugins 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-29"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-28 54 → 2026-10-29 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `667c768beaa0` · [字段定义](../../DATASET.md)*
