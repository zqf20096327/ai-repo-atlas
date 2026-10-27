# shiyubao78/token-sprite

⭐ 26 · JavaScript · NOASSERTION · 推送 2026-10-08 · [GitHub](https://github.com/shiyubao78/token-sprite) · 个人维护 · 中文 README

**读取本地 AI 编程工具 token 用量来养成的桌面小精灵**

基于 Electron 的本地桌宠应用：读取本机 Claude Code（~/.claude/projects）与 Codex（~/.codex rollout 日志）中的真实 token 用量，驱动精灵蛋孵化、五段进化、六条进化线收集、成就抽卡与羁绊系统；附用量洞察面板（按工具/时段统计并折算美元估算）。成长日记功能调用本机已有的 Claude/Codex 回顾当日对话生成知识点与待办，未装 CLI 时可通过复制指令粘给网页版 AI 再回贴。数据全程不上传。需 Node.js 20+，支持 macOS/Windows/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取本地 Claude Code / Codex 日志统计真实 token 用量，全本地不上传
- 五段进化、六条进化线、成就抽卡与稀有度体系（数值可配置调整）
- 成长日记用本机 Claude/Codex 生成知识点与待办，支持拖拽/快捷键投喂内容
- 用量洞察面板：按日/工具/时段统计并折算粗略美元花费

## 适用场景

- 让日常 AI 编程用量变成桌面养成游戏的成长进度
- 查看自己各 AI 编程工具的 token 用量与花费估算
- 每天回顾与 AI 对话中学到的知识点并收集待办

## 场景标签

 · 领域:开发者工具/桌面应用

## 证据(README 行号)

> L218: 应用会自动检测本机支持的 AI 工具，读取本地日志中的 Token 用量。没安装的工具会自动跳过，数据不会离开你的电脑。
> L221: |工具 / Tool|本地读取位置 / Local Data Source|
> L115: 烧 token 不该等于把脑子外包出去。打开**成长日记**，小精灵会用**你本机的 Claude / Codex** 回顾你今天和 AI 的对话，给你：

## 星数曲线

```mermaid
xychart-beta
    title "shiyubao78/token-sprite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `82b75ebdf3a6` · [字段定义](../../DATASET.md)*
