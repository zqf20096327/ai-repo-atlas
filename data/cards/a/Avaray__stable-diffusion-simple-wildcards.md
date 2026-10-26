# Avaray/stable-diffusion-simple-wildcards

⭐ 28 · TypeScript · 推送 2026-03-04 · [GitHub](https://github.com/Avaray/stable-diffusion-simple-wildcards) · 个人维护

**Stable Diffusion 通配词库：为提示词注入随机关键词**

面向 Stable Diffusion 用户的 Wildcards（通配词）合集，主要覆盖含人物的写实场景，也适用于其他类型创作。每条 Wildcard 是一个包含关键词列表的 .txt 文件，在提示词中以 __文件名__ 形式引用，由 Stable Diffusion 随机替换，从而引入随机性。提供 wget/curl/aria2c 一键下载脚本，并给出 Forge/WebUI（需 sd-dynamic-prompts 扩展）、ComfyUI（需 Impact Pack 节点）、Fooocus（原生支持）三种 UI 的安装路径说明。README 提示部分 Wildcards 与 Pony Diffusion 类 checkpoint 不兼容，并列出推荐的 SDXL 写实 checkpoint 与 CFG Scale 参考值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 __文件名__ 语法在提示词中随机替换关键词的 .txt 通配词合集
- 提供 wget/curl/aria2c 自动下载脚本
- 覆盖 Forge/WebUI、ComfyUI、Fooocus 三类 UI 的安装路径说明
- 标注各关键词列表的原始来源与版权信息

## 适用场景

- 生成人物场景时随机化国籍、服装、地点等要素
- 在 Stable Diffusion 各类 UI 中扩充提示词的随机组合能力
- 寻找经过维护清理的关键词列表用于写实风格生成

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L78: A **Wildcard** is essentially a name of a file that contains a list of keywords. If you have a file named `colors.t
> L79: wildcard in your prompt as `__colors__`. Stable Diffusion will replace `__colors__` with a random keyword from the 

## 星数曲线

```mermaid
xychart-beta
    title "Avaray/stable-diffusion-simple-wildcards 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-26 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ac5759102b7a` · [字段定义](../../DATASET.md)*
